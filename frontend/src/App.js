import React, { useState } from 'react';
import {
  Box,
  Container,
  TextField,
  Button,
  Card,
  CardContent,
  Typography,
  CircularProgress,
  Alert,
  Tabs,
  Tab,
  Grid,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material';
import axios from 'axios';

function App() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState(null);
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [selectedTab, setSelectedTab] = useState(0);
  const [categories, setCategories] = useState(['']);
  const [classificationResult, setClassificationResult] = useState(null);

  const handleTabChange = (event, newValue) => {
    setSelectedTab(newValue);
    setResponse(null);
    setClassificationResult(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      if (selectedTab === 0) { // LLM
        const response = await axios.post('http://127.0.0.1:8000/api/v1/llm/generate', {
          prompt: prompt,
          context: {},
          temperature: 0.7
        });
        setResponse(response.data.response.text);
        setMetrics(response.data.metrics);
        setClassificationResult(null);
      } else { // Classification
        const response = await axios.post('http://127.0.0.1:8000/api/v1/classify', {
          text: prompt,
          categories: categories.filter(Boolean)
        });
        setClassificationResult(response.data);
        setMetrics({
          confidence: response.data.confidence,
          latency: response.data.latency || 0
        });
        setResponse(null);
      }
    } catch (err) {
      setError('Failed to process request');
    } finally {
      setLoading(false);
    }
  };

  const handleCategoryChange = (index, value) => {
    const newCategories = [...categories];
    newCategories[index] = value;
    setCategories(newCategories);
  };

  return (
    <Container maxWidth="md" sx={{ mt: 4 }}>
      <Box sx={{ mb: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          AI Quality Assurance Dashboard
        </Typography>
      </Box>

      <Tabs value={selectedTab} onChange={handleTabChange} centered>
        <Tab label="LLM Prompt" />
        <Tab label="Text Classification" />
      </Tabs>

      <Card sx={{ mt: 2 }}>
        <CardContent>
          <form onSubmit={handleSubmit}>
            {selectedTab === 0 ? (
              <TextField
                fullWidth
                label="Enter Prompt"
                variant="outlined"
                margin="normal"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                multiline
                rows={4}
              />
            ) : (
              <>
                <TextField
                  fullWidth
                  label="Enter Text"
                  variant="outlined"
                  margin="normal"
                  value={prompt}
                  onChange={(e) => setPrompt(e.target.value)}
                  multiline
                  rows={2}
                />
                <Box sx={{ mt: 2 }}>
                  {categories.map((category, index) => (
                    <TextField
                      key={index}
                      fullWidth
                      label={`Category ${index + 1}`}
                      value={category}
                      onChange={(e) => handleCategoryChange(index, e.target.value)}
                      sx={{ mb: 2 }}
                    />
                  ))}
                  <Button
                    variant="outlined"
                    onClick={() => setCategories([...categories, ''])}
                    size="small"
                    sx={{ mb: 2 }}
                  >
                    Add Category
                  </Button>
                </Box>
              </>
            )}

            <Button
              type="submit"
              variant="contained"
              color="primary"
              disabled={loading || !prompt}
              sx={{ mt: 2 }}
            >
              {loading ? <CircularProgress size={24} /> : 'Process'}
            </Button>
          </form>

          {error && (
            <Alert severity="error" sx={{ mt: 2 }}>
              {error}
            </Alert>
          )}

          {response || classificationResult ? (
            <Box sx={{ mt: 4 }}>
              <Grid container spacing={3}>
                <Grid item xs={12}>
                  <Typography variant="h6" gutterBottom>
                    {selectedTab === 0 ? 'Response' : 'Classification Result'}:
                  </Typography>
                  {selectedTab === 0 ? (
                    <Typography>{response}</Typography>
                  ) : (
                    <Paper sx={{ p: 2 }}>
                      <Typography>
                        Predicted Category: {classificationResult.category}
                      </Typography>
                      <Table>
                        <TableHead>
                          <TableRow>
                            <TableCell>Category</TableCell>
                            <TableCell align="right">Probability</TableCell>
                          </TableRow>
                        </TableHead>
                        <TableBody>
                          {Object.entries(classificationResult.probabilities).map(
                            ([category, prob]) => (
                              <TableRow key={category}>
                                <TableCell>{category}</TableCell>
                                <TableCell align="right">{prob.toFixed(2)}</TableCell>
                              </TableRow>
                            )
                          )}
                        </TableBody>
                      </Table>
                    </Paper>
                  )}
                </Grid>

                <Grid item xs={12}>
                  <Typography variant="h6" gutterBottom>
                    Metrics:
                  </Typography>
                  <Box sx={{ display: 'flex', gap: 2, mt: 1 }}>
                    {selectedTab === 0 ? (
                      <>
                        <Typography>
                          Accuracy: {metrics?.accuracy?.toFixed(2)}
                        </Typography>
                        <Typography>
                          Hallucination: {metrics?.hallucination?.toFixed(2)}
                        </Typography>
                      </>
                    ) : (
                      <Typography>
                        Confidence: {metrics?.confidence?.toFixed(2)}
                      </Typography>
                    )}
                    <Typography>
                      Latency: {metrics?.latency?.toFixed(2)}s
                    </Typography>
                  </Box>
                </Grid>
              </Grid>
            </Box>
          ) : null}
        </CardContent>
      </Card>
    </Container>
  );
}

export default App;
