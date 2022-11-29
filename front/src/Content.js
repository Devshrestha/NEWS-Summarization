import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';

export default function Content() {
  return (
      <Grid container rowSpacing={5} columnSpacing={{ xs: 12, sm: 12, md: 2 }} >
      {Array.from(Array(6)).map((_, index) => (
      <Grid item xs={2} sm={4} md={4} key={index}>
        <Paper>
          df
        </Paper>
      </Grid>
        ))}
    </Grid>
    // <Paper sx={{ maxWidth: 936, margin: 'auto', overflow: 'hidden' }}>
    //   <AppBar
    //     position="static"
    //     color="default"
    //     elevation={0}
    //     sx={{ borderBottom: '1px solid rgba(0, 0, 0, 0.12)' }}
    //   >
    //   </AppBar>
    //   <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
    //       <Grid item xs={6} md ={4}>
    //           1
    //       </Grid>
    //       <Grid item xs={6}>
    //         2
    //       </Grid>
    //       <Grid item xs={6}>
    //         3
    //       </Grid>

    //     </Grid>
    // </Paper>
  );
}