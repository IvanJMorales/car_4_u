import React from "react";
import truck from "./thumbnail/truck.jpeg";
import Carousel from 'react-bootstrap/Carousel';

const Trucks = () => {
  return (
    <div className="Trucks-section">
      <div className="container">
        <div className="row">
          <header className="App-header">
            <h1>Trucks Details</h1>
          </header>
          <div className="col-md-3"></div>
          <div className="col-md-6">
            <div class="col">
              <div class="card h-100">
                {/* <img src={truck} class="card-img-top" /> */}
                <Carousel>
                  <Carousel.Item>
                    <img
                      className="d-block w-100"
                      src={truck}
                      alt="First slide"
                    />
                  </Carousel.Item>
                  <Carousel.Item>
                    <img
                      className="d-block w-100"
                      src="https://media.istockphoto.com/id/1284419710/photo/white-truck-in-motion-uk-street.jpg?s=612x612&w=0&k=20&c=kefsqF_whlTTjqRDkWtju-Z8PEdiA01EhERNQTrOUkw= "
                      alt="Second slide"
                    />
                  </Carousel.Item>
                  <Carousel.Item>
                    <img
                      className="d-block w-100"
                      src="https://c8.alamy.com/comp/CET43E/brightly-colored-trucks-in-islamabad-pakistan-CET43E.jpg"
                      alt="Third slide"
                    />
                  </Carousel.Item>
                </Carousel>
                <div class="card-body">
                  <h5 class="card-title">
                    {" "}
                    <strong>TRUCK</strong>{" "}
                  </h5>
                  <p class="card-text">
                    This is a longer card with orting Some users may want a
                    luxurious car with great horsepower as well, but more
                    impressive for taking a lady out on a date. That car can be
                    a Mercedes, BMW, Audi, Infiniti, or any other similar car
                    with leather seats, V6 or V8 engine, tinted windows, and
                    makes loud noises when it drives. By filtering out cars with
                    tinted windows, luxury category, price, color, and
                    horsepower which makes the car roam louder when it drives
                    faster, our user will be happy to know they have so many
                    varieties to choose from and can narrow it down with any
                    more specific details that they would like.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div className="col-md-3"></div>
        </div>
      </div>
    </div>
  );
};

export default Trucks;
