import React, { useState } from 'react';
import axios from 'axios';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.css'; 
import DataTable from './DataTable';

function CompanyInfoTable(){
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [statusMessage, setStatusMessage] = useState('No data to display. Click "Scrape Data".');
  const fetchData = async () => {
    setLoading(true);
    setStatusMessage("Loading...");
    try {
      const response = await axios.get("http://127.0.0.1:5000/scrape");
      setData(response.data.data);
      setStatusMessage("Data fetched successfully.");
    } catch (error) {
      console.error("Error fetching data", error);
      setLoading(false);
      setStatusMessage("Some error occurred. Please try again later.");
    }
    setLoading(false);
  };

  return (
    <div className="App">
        <center>
      <h1 className='bold'>COMPANY INFO SCRAPPER</h1>
      <Button size='md' variant="success" className='mt-3' onClick={fetchData} disabled={loading}>
        Scrape Data
      </Button>
      </center>
      <div className='mt-3'>
        <center>
          <p>
            <div>
              <p>{statusMessage}</p>
              </div>
              </p>
          </center>
        {data.length > 0 && <DataTable data={data} />}
      </div>
    </div>
  );

}


export default CompanyInfoTable;