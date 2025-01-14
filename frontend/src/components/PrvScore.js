import React from 'react';
import './styles/PrvScore.css';

export default function PrvScore() {
  return (
    <div className='table-container my-5'>
      <h1 className="table-heading">Previous Scores</h1>
      <div className='table-wrapper'>
        <table className="styled-table">
          <thead>
            <tr>
              <th scope="col">S.No</th>
              <th scope="col">Player Name</th>
              <th scope="col">Target Word</th>
              <th scope="col">Predicted Words</th>
              <th scope="col">Max Similarity Score</th>

            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td>Rishi Jain</td>
              <td>Tiger</td>
              <td>Tigress, Cheetah, Elephant...</td>
              <td>0.89</td>

            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
