// Update the API URL to point to your server's API endpoint
const API_URL = '/api/chat'; // Assuming your server is running on the same domain

// ...

chatInput.addEventListener('keydown', async (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();

    const userMessage = chatInput.value.trim();

    if (!userMessage) return;

    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ userMessage }),
    });

    const data = await response.json();

    // Append the chatbot's response to the chatbox
    const chatLi = createChatLi(data.choices[0].message.content.trim(), 'incoming');
    chatbox.appendChild(chatLi);

    // Clear the input
    chatInput.value = '';
    chatbox.scrollTo(0, chatbox.scrollHeight);
  }
});
