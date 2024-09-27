import React from "react";
import luxury from "./thumbnail/luxury.jpeg";
import Carousel from 'react-bootstrap/Carousel';

const Luxurys = () => {
  return (
    <div className="Luxurys-section">
      <div className="container ">
        <div className="row">
          <header className="App-header">
            <h1>LUXURYS Details</h1>
          </header>
          <div className="col-md-3"></div>
          <div className="col-md-6">
            <div class="col mb-5">
              <div class="card h-100 "  >
                {/* <img src={luxury} className="card-img-top" /> */}
                <Carousel>
                  <Carousel.Item>
                    <img
                      className="d-block w-100"
                      src={luxury}
                      alt="First slide"
                    />
                  </Carousel.Item>
                  <Carousel.Item>
                    <img
                      className="d-block w-100"
                      src="https://images.pexels.com/photos/3764984/pexels-photo-3764984.jpeg?cs=srgb&dl=pexels-jae-park-3764984.jpg&fm=jpg"
                      alt="Second slide"
                    />
                  </Carousel.Item>
                  <Carousel.Item>
                    <img
                      className="d-block w-100"
                      src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5ZB8ZcX7mSJo-0j5m00xSIpg2pfbz0cegY1kfn03mxtSOHfvdsiWwXEvgaFs4RSx9zJI&usqp=CAU"
                      alt="Third slide"
                    />
                  </Carousel.Item>
                </Carousel>
                <div class="card-body">
                  <h5 class="card-title text-black">
                    <strong>LUXURY</strong>
                  </h5>
                  <p class="card-text text-black mb-3">
                    Our project allows the user to filter out what exactly they
                    want in their car or how it performs, which then filters
                    through various databases from different car companies and
                    compares the best options for them. For example, a user may
                    own a construction company and needs a strong, sturdy truck
                    that has great trunk space, and is capable of driving in
                    heavy snow, rain, and even withstand hail. The user will
                    instantly have access to many different trucks with the
                    features and specs they need their truck to be able to have,
                    as well as price range, mileage, capability, and horsepower.{" "}
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

export default Luxurys;
