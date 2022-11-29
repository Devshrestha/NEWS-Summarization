import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Grid from '@mui/material/Grid';
import Tab from '@mui/material/Tab';
import Tabs from '@mui/material/Tabs';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';

const lightColor = 'rgba(255, 255, 255, 1)';

function Header(props) {

  return (
    <React.Fragment>
      <AppBar
        component="div"
        color="primary"
        position="static"
        elevation={0}
        sx={{ zIndex: 0,bgcolor: "#1e7b7b" }}
      >
        <Toolbar>
          <Grid container alignItems="center" spacing={1}>
            <Grid item xs>
              <Typography color="inherit" variant="h5" component="h1">
                Lightning NEWS
              </Typography>
            </Grid>
          </Grid>
        </Toolbar>
      </AppBar>
      <AppBar component="div" position="static" elevation={0} sx={{ zIndex: 0,bgcolor: "#1e7b7b" }}>
        <Tabs value={0} textColor="inherit">
          <Tab label="Home" />
          <Tab label="International" />
          <Tab label="National" />
          <Tab label="Sports" />
          <Tab label="Technology" />
        </Tabs>
      </AppBar>
    </React.Fragment>
  );
}


export default Header;