import React, { useEffect, useState } from 'react';
import { Card, Table } from 'react-bootstrap';

const Leaderboard = () => {
  const [leaders, setLeaders] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Fetching Leaderboard from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = Array.isArray(data) ? data : data.results || [];
        setLeaders(results);
        console.log('Fetched Leaderboard:', data);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  return (
    <Card className="mb-4 shadow-sm">
      <Card.Body>
        <Card.Title as="h2" className="mb-4">Leaderboard</Card.Title>
        <Table striped bordered hover responsive>
          <thead>
            <tr>
              {leaders[0] && Object.keys(leaders[0]).map((key) => (
                <th key={key}>{key}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {leaders.map((leader, idx) => (
              <tr key={leader.id || idx}>
                {Object.values(leader).map((val, i) => (
                  <td key={i}>{typeof val === 'object' ? JSON.stringify(val) : val}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </Table>
        {leaders.length === 0 && <div className="text-muted">No leaderboard data found.</div>}
      </Card.Body>
    </Card>
  );
};

export default Leaderboard;
