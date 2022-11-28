import React from "react";
import { Link } from "react-router-dom";
import './App.css';

import luxury from './thumbnail/luxury.jpeg';

const Home = () => {
  const data = [
    {
      imag: "./Assists/cars1.jpeg",
      Title: "Car",
      text: "Some users don’t really have a specific car in mind, but just want to buy a car because it's time. There are many great options such as Toyota, Honda, Nissan, Hyundai, and others that are affordable, last many years, don’t break down so easily, and are the perfect types of car to get started with. We can have a basic filter that gives them such options as well as basic needs such as heating, air conditioning, trunk space, number of miles per gallon, whether the car is electric or hybrid or combustion engine. Our user will be delighted to know that they won’t have to search individually anymore, but have all those options right by their fingertips.",
      rout:"car",
    },
    {
      imag: luxury,
      Title: "LUXURY",
      text: "Our project allows the user to filter out what exactly they want in their car or how it performs, which then filters through various databases from different car companies and compares the best options for them. For example, a user may own a construction company and needs a strong, sturdy truck that has great trunk space, and is capable of driving in heavy snow, rain, and even withstand hail. The user will instantly have access to many different trucks with the features and specs they need their truck to be able to have, as well as price range, mileage, capability, and horsepower. ",
      rout: "luxury",
    },
    {
      imag: "./Assists/truck2.webp",
      Title: "TRUCK",
      text: "This is a longer card with orting Some users may want a luxurious car with great horsepower as well, but more impressive for taking a lady out on a date. That car can be a Mercedes, BMW, Audi, Infiniti, or any other similar car with leather seats, V6 or V8 engine, tinted windows, and makes loud noises when it drives. By filtering out cars with tinted windows, luxury category, price, color, and horsepower which makes the car roam louder when it drives faster, our user will be happy to know they have so many varieties to choose from and can narrow it down with any more specific details that they would like.",
      rout: "truck",
    },
  ];
  return (
    <>
      <header className="App-header">
        <h1>Right Car For You</h1>
      </header>
      <main>
        <div class="row row-cols-1 row-cols-md-3 g-4">
          {data.map((value, i) => {
            return (
              <>
                <div class="col">
                  <div
                    class="card h-100 back  text-black"
                  >
                    <img src={value.imag} className="card-img-top h-75" />
                    <div class="card-body">
                      <h5 class="card-title">
                        <strong>{value.Title}</strong>
                      </h5>
                      <p
                        class="card-text text-white"
                      >
                        {value.text.slice(0, 133)}....
                      </p>
                      <Link className="btn text-black" to={value.rout}>For More Detail</Link>
                    </div>
                  </div>
                </div>
              </>
            );
          })}
        </div>
      </main>
    </>
  );
};

export default Home;
