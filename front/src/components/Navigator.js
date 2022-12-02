import * as React from 'react';
import { Link } from "react-router-dom";
import Divider from '@mui/material/Divider';
import Drawer from '@mui/material/Drawer';
import List from '@mui/material/List';
import Box from '@mui/material/Box';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import HomeIcon from '@mui/icons-material/Home';
import PublicIcon from '@mui/icons-material/Public';
import LocationOnOutlinedIcon from '@mui/icons-material/LocationOnOutlined';
import SportsSoccerOutlinedIcon from '@mui/icons-material/SportsSoccerOutlined';
import DevicesOutlinedIcon from '@mui/icons-material/DevicesOutlined';


const categories = [
  {
    id: 'Categories',
    children: [
      {id:'Home',icon:<HomeIcon />, link:'/'},
      { id: 'International', icon: <PublicIcon />, link:'/inter'},
      {
        id: 'National',
        icon: <LocationOnOutlinedIcon />,
        active: true,
        link: '/national'
      },
      { id: 'Sports', icon: <SportsSoccerOutlinedIcon />, link: '/sport' },
      { id: 'Technology', icon: <DevicesOutlinedIcon />, link: '/tech' },
      ,
    ],
  },
  
];

const item = {
  py: '2px',
  px: 3,
  color: 'rgba(255, 255, 255, 0.7)',
  '&:hover, &:focus': {
    bgcolor: 'rgba(255, 255, 255, 0.08)',
  },
};

const itemCategory = {
  boxShadow: '0 -1px 0 rgb(255,255,255,0.1) inset',
  py: 1.5,
  px: 3,
};

export default function Navigator(props) {
  const { ...other } = props;

  return (
    <Drawer variant="permanent" {...other}>
      <List disablePadding>
        <ListItem sx={{ ...item, ...itemCategory, fontSize: 22, color: '#fff' }}>
          Lightning NEWS
        </ListItem>
        <ListItem sx={{ ...item, ...itemCategory }}>

        </ListItem>
        {categories.map(({ id, children }) => (
          <Box key={id} sx={{ bgcolor: '#101F33' }}>
            <ListItem sx={{ py: 2, px: 3 }}>
              <ListItemText sx={{ color: '#fff' }}>{id}</ListItemText>
            </ListItem>
            {children.map(({ id: childId, icon, active,link }) => (
              <ListItem disablePadding key={childId}>
                <Link to={link} style={{ textDecoration: 'none' }}>
                <ListItemButton selected={active} sx={item}>
                  <ListItemIcon>{icon}</ListItemIcon>
                  <ListItemText>{childId}</ListItemText>
                </ListItemButton>
                </Link>
              </ListItem>
            ))}

            <Divider sx={{ mt: 2 }} />
          </Box>
        ))}
      </List>
    </Drawer>
  );
}