import React, { useEffect, useState } from 'react';
import "../styles/SearchPage.css";


import { collection, getDocs } from "firebase/firestore";
import { database } from '../firebase.js';


import SearchField from "./SearchField";
import SearchResultsCard from "./SearchResultsCard";

import Pagination from '@mui/material/Pagination';


const SearchPage = () => {
    // Create state for cars
    const [cars, setCars] = useState([]);
    // Grab Vehicles collection from Firestore Database
    const collectionRef = collection(database, "Vehicles")

    // Grab each Document in Vehicle Collection from Firestore Database
    useEffect(() => {
        const getData = async () => {
            const data = await getDocs(collectionRef);
            setCars(data.docs.map((doc) => ({ ...doc.data(), id: doc.id })))
            console.log(data)
        };

        getData();
    }, []);


    return (
        <div>
            <div className="primary-search-container">
                <SearchField 
                    cars={cars}
                />
            </div>
            <SearchResultsCard 
                cars={cars}
            />
            <Pagination count={10} />
        </div>
    )
}

export default SearchPage