import Footer from "./components/Footer";
import Header from "./components/Header";
import {Routes, Switch, Route} from "react-router-dom";
import HomePage from "./components/HomePage";
import SearchPage from "./components/SearchPage";
import HowItWorks from "./components/HowItWorks";
import RightCar4U from "./components/RightCar4U";
import "./App.css";
import CarInfo from "./components/CarInfo";

function App() {
  return (
    <div>
      <Header />
        <Routes>
                <Route path="/" element={<HomePage />}/>
                <Route path="/search-page" element={<SearchPage />}/>
                <Route path="/how-it-works" element={<HowItWorks />}/>
                <Route path="/right-car-for-you" element={<RightCar4U />}/>
                <Route path="/car-info/:id" element={<CarInfo />}/>
        </Routes>
      <Footer />
    </div>
  )
}

export default App;
