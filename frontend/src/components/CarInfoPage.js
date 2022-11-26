import React, { useState, useEffect, useContext } from 'react';
import '../styles/CarInfo.css';

import { Link, useParams } from 'react-router-dom';

// Firebase imports
import { doc, getDoc } from "firebase/firestore";


import { database } from '../firebase.js';
import { CollectionContext } from '../App';


const CarInfo = () => {
    // Create state for car selected
    const [carState, setCarState] = useState('');

    // Get car id from end of URL
    const carId = useParams();
    //console.log("CAR ID PARAM:", carId.id)

    // Get Collection Contexts from "./App"
    const collection = useContext(CollectionContext)

    // Reference document based on carId
    const docRef = doc(database, "Vehicles", carId.id)

    // Get snapshot from firebase set to docSnap, set carState to docSnap data
    useEffect(() => {
        const getCarData = async () => {
            const docSnap = await getDoc(docRef);
            //console.log(docSnap.data());
            setCarState(docSnap.data())
        };
        getCarData();
    }, []);

    return (
        <div className='carInfo-container'>
            {carState.Name}
            <br></br>
            {carState.Miles}
            <img 
            src={carState.Image}
            alt="new"
            />
        </div>
    );
};

export default CarInfo;