import React, { useState } from 'react';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async () => {
    try {
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: prompt }),
      };

      const response = await fetch('/api/get_response', requestOptions);
      const data = await response.json();

      if (data.response) {
        setResponse(data.response);
      } else {
        console.error('Error:', data.error);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>React GPT🤖</h1>
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt"
        />
        <button onClick={handleSubmit}>Get Response</button>
        {response && (
          <div>
            <h2>Response:</h2>
            <p>{response}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
