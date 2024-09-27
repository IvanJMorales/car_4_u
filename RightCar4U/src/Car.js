import React from 'react'
import car from './thumbnail/car.jpeg';
import './App.css';
import Carousel from 'react-bootstrap/Carousel';
const Car = () => {
  return (
    <div className="Car-section">
        <div className="container">
            <div className="row">
            <header className="App-header">
        <h1>Cars Details</h1>
      </header>
                <div className="col-md-3"></div>
                <div className="col-md-6">
                <div class="col">
            <div class="card h-100">
              {/* <img src={car} className="card-img-top" /> */}
              <Carousel>
                  <Carousel.Item>
                    <img
                      className="d-block w-100"
                      src={car}
                      alt="First slide"
                    />
                  </Carousel.Item>
                  <Carousel.Item>
                    <img
                      className="d-block w-100"
                      src="https://sharazicars.pk/wp-content/uploads/2022/04/Toyota-Car-Prices-in-Pakistan.jpg"
                      alt="Second slide"
                    />
                  </Carousel.Item>
                  <Carousel.Item>
                    <img
                      className="d-block w-100"
                      src="https://img.dunyanews.tv/news/2018/October/10-17-18/news_big_images/462458_88069817.jpg"
                      alt="Third slide"
                    />
                  </Carousel.Item>
                </Carousel>
              <div class="card-body">
                <h5 class="card-title"><strong>CAR</strong></h5>
                <p class="card-text">
                Some users don’t really have a specific car in mind, but just want to buy a car because it's time. There are many great options such as Toyota, Honda, Nissan, Hyundai, and others that are affordable, last many years, don’t break down so easily, and are the perfect types of car to get started with. We can have a basic filter that gives them such options as well as basic needs such as heating, air conditioning, trunk space, number of miles per gallon, whether the car is electric or hybrid or combustion engine. Our user will be delighted to know that they won’t have to search individually anymore, but have all those options right by their fingertips. 
                </p>
              </div>
            </div>
          </div>
                </div>
                <div className="col-md-3"></div>
            </div>
        </div>
    </div>
  )
}

export default Car