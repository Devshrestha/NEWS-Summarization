import * as React from 'react';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Divider from '@mui/material/Divider';
import { useEffect, useState } from 'react';
import DataService from "../services/DataService";

export default function Content() {
    let [summaries, setSummaries] = useState([]);
    const get_sum_api = () => {
        DataService.GetNat()
            .then(function (response) {
              setSummaries(response.data);
              summaries=response;
            });
          }
      // Setup Component
      useEffect(() => {
        get_sum_api();
      }, []);
    
      console.log()
  
  
    return (
        <Grid container rowSpacing={5} columnSpacing={{ xs: 6 ,sm:12}} >
        {summaries.map((news, index) => (
        <Grid item xs={6} sm={12}  key={index} justifyContent="center">
          <Paper elevation={3} style={{padding:10,border: "1px solid black"}}>
  
            <h3>{JSON.stringify(news['hed'])}</h3>
            <Divider />
            <h5 style={{color: "#595959"}}>{JSON.stringify(news['sum'])}</h5>
            <br></br>
          </Paper>
        </Grid>
          ))}
      </Grid>
    
    );
  }