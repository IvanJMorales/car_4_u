import "mdb-react-ui-kit/dist/css/mdb.min.css";
//import "@fortawesome/fontawesome-free/css/all.min.css";

import "../styles/RightCar4U.css";

import { BrowserRouter, Route, Routes } from "react-router-dom";
import Car from "./Car";
import Home from "./Home";
import Trucks from "./Trucks";
import Luxurys from "./Luxurys";

function RightCarForU() {
  return (
  <div>
      <div class="hero-section">
      <div class="hero-section-text">
       <h1>Contact Us For The Right Car 4 U</h1>
        <p>We can help you to gain access to any and every car.<br></br>
          Contact us below and we can help you get started!<br></br>
        </p>
       </div>
</div>



<div>
<div class="social-links">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" rel="stylesheet"/>

  <div class="row">
    <div class="small-6 medium-3 columns text-center mobile-stack">
      <a href="https://www.facebook.com/"><i class="fa fa-facebook" aria-hidden="true"></i>Facebook</a>
      <a href="https://www.instagram.com/?hl=en"><i class="fa fa-instagram" aria-hidden="true"></i>Instagram</a>
      <a href="https://www.pinterest.com/"><i class="fa fa-pinterest-p" aria-hidden="true"></i>Pinterest</a>
      <a href="https://twitter.com/?lang=en"><i class="fa fa-twitter" aria-hidden="true"></i>Twitter</a>
    </div>
</div>
</div>
</div>


    </div>
  );
}

export default RightCarForU;
