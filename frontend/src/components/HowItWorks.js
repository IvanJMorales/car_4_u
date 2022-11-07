import img1 from '../images/1.png'
import img2 from '../images/2.png'

import '../styles/HowItWorks.css';

function HowItWorks() {
  return (
    <div className='App'>
      <header className="App-header">
        <p>
        For our Cars 4 U Website, we are using React.js along with Django and Python to read and extract .json files from car datasets. This allows us to have access to many different cars with different attributes from various datasets. It is filtered by milage, whether the car is combustion engine or electric, make or model, and so on. The front end part of the website uses React and has a navbar that allows the user to find what they need and filter anthing else out. This makes it easier when searching for a car.
        </p>

      <img src={img1} width = "300px" height = "200px" />
      <img src={img2} width = "300px" height = "200px" />


      </header>
    </div>
  );
}

export default HowItWorks;
