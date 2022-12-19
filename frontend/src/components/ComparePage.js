import React from 'react';
import { useLocation } from 'react-router';

import '../styles/ComparePage.css';

// MUI Imports
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';

import { Divider } from '@mui/material';

import { Link, useNavigate } from 'react-router-dom';

const ComparePage = () => {
    const carsToCompare = useLocation()

    console.log(carsToCompare)
    return (
        <div className='compare-field'>
            {carsToCompare.state.compareCars.slice(0,20).map((car) => (
                <Box className='compare-box' sx={{ width: '100%'}}>
                    <Stack direction='row' divider={<Divider orientation='vertical' flexItem />}spacing={2}>
                    <img src={car.Image}></img>
                    <div className='carInfo'>{car.Name}</div>
                    <div className='carInfo'>{car.Manufacturer}</div>
                    <div className='carInfo'>{car.Model}</div>
                    <div className='carInfo'>{car.Year}</div>
                    <div className='carInfo'>{car.Miles}</div>
                    <div className='carInfo'>{car.Color}</div>
                    <div className='carInfo'>{car.Engine}</div>
                    </Stack>
                </Box>
            )
            )}
        </div>
    );
};

export default ComparePage;