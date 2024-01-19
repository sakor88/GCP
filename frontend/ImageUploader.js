import React, { useState } from 'react';
import axios from 'axios';

const ImageUploader = () => {
  const [uploadedFile, setUploadedFile] = useState(null);
  const [uploadMessage, setUploadMessage] = useState('');

  const onFileChange = async (e) => {
    const file = e.target.files[0];

    if (file) {
      const reader = new FileReader();
      reader.onload = async (event) => {
        const fileData = event.target.result.split(',')[1];
        try {
          const response = await uploadImage(fileData, file.name);

          if (response.status === 200) {
            setUploadedFile(response.data.publicUrl);
            setUploadMessage(`File uploaded successfully! Response: ${JSON.stringify(response.data)}`);
          } else {
            setUploadMessage(`Error uploading file: ${response.data}`);
          }
        } catch (error) {
          console.error('Error uploading file:', error);
          setUploadMessage('Error uploading file.');
        }
      };

      reader.readAsDataURL(file);
    }
  };

  const uploadImage = async (file, fileName) => {
    const fmData = new FormData();
    fmData.append('image', file);
    fmData.append('fileName', fileName);

    try {
      const response = await axios.post(
        'https://europe-west2-gcp-final-project-410222.cloudfunctions.net/backend/',
        fmData,
        {
          headers: { 'Content-Type': 'multipart/form-data' },
        }
      );

      return response;
    } catch (err) {
      console.log('Error: ', err);
      throw err;
    }
  };

  return (
    <div>
      <input type="file" onChange={onFileChange} />
      {uploadMessage && <p>{uploadMessage}</p>}
      {uploadedFile && (
        <div>
          <img
            src={uploadedFile}
            alt="Uploaded"
            style={{ maxWidth: '100%', maxHeight: '400px', marginTop: '20px' }}
          />
        </div>
      )}
    </div>
  );
};

export default ImageUploader;
