import React from 'react';
import ReactDOM from 'react-dom';
import ImageUploader from './ImageUploader';

const App = () => {
  return (
    <div>
      <ImageUploader />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
