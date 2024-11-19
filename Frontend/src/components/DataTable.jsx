import React from 'react';
import Table from 'react-bootstrap/Table';

function DataTable({ data }) {
  return (
    <Table striped bordered hover responsive>
      <thead>
        <tr>
          <th>Company</th>
          <th>Description</th>
          <th>URL</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item, index) => (
          <tr key={index}>
            <td>{item.company}</td>
            <td>{item.data}</td>
            <td>
              <a target="_blank" rel="noreferrer" href={item.url}>
                Click
              </a>
            </td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
}

export default DataTable;
