import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [predictions, setPredictions] = useState([]);

    useEffect(() => {
        axios.get('/api/predictions')
            .then(response => {
                setPredictions(response.data);
            })
            .catch(error => {
                console.error('Error fetching predictions:', error);
            });
    }, []);

    return (
        <div className="App">
            <h1>KAIScaler Dashboard</h1>
            <table>
                <thead>
                    <tr>
                        <th>Timestamp</th>
                        <th>Predicted CPU Usage</th>
                    </tr>
                </thead>
                <tbody>
                    {predictions.map((prediction, index) => (
                        <tr key={index}>
                            <td>{prediction.timestamp}</td>
                            <td>{prediction.cpu_usage}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default App;