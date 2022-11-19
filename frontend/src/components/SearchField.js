import React, { useEffect, useState } from "react";
import "../styles/SearchField.css";

import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import Slider from '@mui/material/Slider';
import Box from '@mui/material/Box';

function SearchField(props) {
    console.log(props.cars)

    // Variable to check for duplicates of Manufacturers
    const manuDuplicateCheck = []
    const yearDuplicateCheck = []

    props.cars.sort((a,b) => a.Name.localeCompare(b.Name))
    console.log(props.cars)


    return (
        <div className="selection-area">
            <div className="selectors">

                {/***** Manufacturer of car selector *****/}
                <TextField
                    id="make"  
                    select
                    label="Make"
                    //value={carMake}
                    //onChange={//handleMakeChange}
                    helperText="Manufacturer"
                    prop sx={{width: 120}}
                >
                    <div className="options">
                        {props.cars.map((car) => {
                            // Check for duplicates in Manufacturer
                            if (manuDuplicateCheck.includes(car.Manufacturer)) {
                                return null;
                            }
                            manuDuplicateCheck.push(car.Manufacturer);
                            
                            // Render card for each car in array
                            return (
                                <MenuItem className='menu-item' key={car.id}>
                                    {car.Manufacturer}
                                </MenuItem>
                            )
                        })}
                    </div>
                </TextField>



                {/***** Year of car selector *****/}
                <TextField
                    id="year"  
                    select
                    label="Year"
                    //value={carMake}
                    //onChange={//handleMakeChange}
                    helperText="Year"
                    prop sx={{width: 120}}
                >
                    <div className="options">
                        {props.cars.map((car) => {
                            // Check for duplicates in Manufacturer
                            if (yearDuplicateCheck.includes(car.Year)) {
                                return null;
                            }
                            yearDuplicateCheck.push(car.Year);
                            
                            // Render card for each car in array
                            return (
                                <MenuItem className='menu-item' key={car.id}>
                                    {car.Year}
                                </MenuItem>
                            )
                        })}
                    </div>
                </TextField>



                {/***** Price of car selector *****/}
                <TextField
                    id="price"  
                    select
                    label="Price"
                    //value={carMake}
                    //onChange={//handleMakeChange}
                    helperText="Price"
                    prop sx={{width: 120}}
                >
                    <Slider></Slider>
                </TextField>
            </div>
        </div>
    );
};

export default SearchField;