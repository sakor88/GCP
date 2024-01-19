// App.js
import React from 'react';
import ImageUploader from './ImageUploader';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Google Cloud Vision Facial Expression Evaluator</h1>
        <ImageUploader />
        <div id="objectResponse"></div>
      </header>
    </div>
  );
}

export default App;