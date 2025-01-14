import React from 'react';
import './styles/Instructions.css'; 

export default function Instructions() {
  return (
    <div className="instructions-container my-5">
      <h1 className="heading">How to Play the Game</h1>

      <div className="instructions-content">
        <h2 className="instruction-item">
          - Choose your preferred language (English, Hindi, or any).
        </h2>
        <h2 className="instruction-item">
          - Enter a word in the selected language and category.
        </h2>
        <h2 className="instruction-item">
          - Click the Submit button, and the game will provide feedback:
        </h2>
        <h2 className="instruction-item">
          - Similarity score (ranges from 0 to 1).
        </h2>
        <h2 className="instruction-item">
          - You have a total of 5 attempts to guess the word correctly.
        </h2>
      </div>
    </div>
  );
}
