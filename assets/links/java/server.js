const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios'); // HTTP client for making requests

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

// API endpoint to handle chatbot requests
app.post('/api/chat', async (req, res) => {
  try {
    const userMessage = req.body.userMessage;
    const API_KEY = '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';
    const API_URL = 'https://api.openai.com/v1/chat/completions';

    const response = await axios.post(API_URL, {
      model: 'gpt-3.5-turbo',
      messages: [{ role: 'user', content: userMessage }],
    }, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${API_KEY}`,
      },
    });

    res.json(response.data);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Something went wrong.' });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
