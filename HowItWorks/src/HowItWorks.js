import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle";
// import { BrowserRouter,Routes, Route } from 'react-router-dom';
// import Base from './Components/Layout/Base';
// import Home from "./Pages/Home"
import img1 from './HowItWorks-pics/1.png'
import img2 from './HowItWorks-pics/2.png'

import "./HowItWork.scss";

function HowItWorks() {
  return (
    <div className="App">
      <div className="container text-center text-white mt-5">
        <div className="row">
          <h1>Project Details</h1>
          <div className="col-md-2"></div>
          <div className="col-md-8">
          <header className="App-header bg-primary p-5 rounded-5 text-start " style={{backgroundColor:"orange !important"}}>
        <p>
          For our Cars 4 U Website, we are using React.js incoroporated with
          Django and python to read and extract .csv files from car datasets.
          This allows us to have access to many different caars with different
          attributes from various datasets. We are also using .json files to
          fetch the .csv file and convert it so that the uer has all the data
          and information needed for when they search what kind of car they
          want. It is filtered by milage, whether the car is combustion engine
          or electric, make of model, and so on. We actually connect the user to
          the datbase itself through Django and extrct through React so it's
          user friendly. The front end part of the website uses React and has a
          navbar the allows the user to find what they need and filter anthing
          else out. This makes it easier when getting a car.
        </p>

        <img src={img1} className="mt-4" width="100%"  />
        <img src={img2} className="mt-4" width="100%"  />
      </header>
          </div>
          <div className="col-md-2"></div>
        </div>
      </div>
      
    </div>
  );
}

export default HowItWorks;
