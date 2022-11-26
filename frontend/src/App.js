import React, { useEffect, useState, createContext, useContext } from 'react';

import Footer from "./components/Footer";
import Header from "./components/Header";
import {Routes, Switch, Route} from "react-router-dom";
import HomePage from "./components/HomePage";
import SearchPage from "./components/SearchPage";
import HowItWorks from "./components/HowItWorks";
import RightCar4U from "./components/RightCar4U";
import SearchResultsBody from './components/SearchResultsBody';
import "./App.css";
import CarInfoPage from "./components/CarInfoPage";
//import LoginScreen from "./components/LoginScreen"
//import RegisterScreen from "./components/RegisterScreen"
import Loader from "./components/Loader"

import { collection, getDocs } from "firebase/firestore";
import { database } from './firebase.js';


// Collection Reference Context to make Collection accessable to all Context wrapped components
export const CollectionContext = createContext()

const collectionRef = collection(database, "Vehicles")


console.log(collectionRef)
function App() {
  return (
    <div>
      <CollectionContext.Provider value={collectionRef}>
      <Header />
        <Routes>
          <Route path="/" element={<HomePage />}/>
          <Route path="/search-page" element={<SearchPage />}/>
          <Route path="/how-it-works" element={<HowItWorks />}/>
          <Route path="/right-car-for-you" element={<RightCar4U />}/>
          <Route path="/car-info/:id" element={<CarInfoPage />}/>
          <Route path="/search-results/" element={<SearchResultsBody />}/>
        </Routes>
      <Footer />
      </CollectionContext.Provider>
    </div>
  )
}

export default App;
