//import "bootstrap/dist/css/bootstrap.min.css";
//import "bootstrap/dist/js/bootstrap.bundle";
import img1 from '../images/1.png'
import img2 from '../images/2.png'
//import "../styles/HowItWorks.css"


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
          For our Car 4 U Website, we are using React.js incoroporated with
          Firebase and Python to read and extract data from car datasets.
          This allows us to have access to many different cars with different
          attributes from various datasets. We are using a Python based web scrapper to retrieve
          data from multiple used car sale sites to populate our Firebase Firestore database.
          From there we use the Firestore API to pull data and present it to the you so that you many
          find the right Car 4 U.
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
