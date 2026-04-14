import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/workouts/`
    : 'http://localhost:8000/api/workouts/';

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Workouts endpoint:', endpoint);
        console.log('Fetched workouts:', results);
      });
  }, [endpoint]);

  return (
    <div>
      <h2 className="mb-4 text-danger fw-bold">Workouts</h2>
      <div className="card shadow-sm">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead className="table-danger">
              <tr>
                <th>User</th>
                <th>Workout</th>
                <th>Reps</th>
              </tr>
            </thead>
            <tbody>
              {workouts.map((w, i) => (
                <tr key={i}>
                  <td>{w.user}</td>
                  <td>{w.workout}</td>
                  <td>{w.reps}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Workouts;
