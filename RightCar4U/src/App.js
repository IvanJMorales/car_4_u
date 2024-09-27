import "mdb-react-ui-kit/dist/css/mdb.min.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

import "./App.css";

import { BrowserRouter, Route, Routes } from "react-router-dom";
import Car from "./Car";
import Home from "./Home";
import Trucks from "./Trucks";
import Luxurys from "./Luxurys";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Home" element={<Home />} />

          <Route path="/car" element={<Car />} />
          <Route path="/luxury" element={<Luxurys />} />

          <Route path="/truck" element={<Trucks />} />
        </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;
