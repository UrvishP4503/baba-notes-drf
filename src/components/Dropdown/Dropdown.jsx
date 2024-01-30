import { useState } from "react";
import { Link } from "react-router-dom";
import "./Dropdown.css";

const Dropdown = () => {
  const [isOpen, setIsOpen] = useState(false);

  const handleClick = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="dropdown">
      <button className="dropdown-button" onClick={handleClick}>
        bobobo is {isOpen ? "open" : "closed"}
      </button>
      <div className="dropdown-menu">
        {isOpen && (
          <div>
            <Link className="catagories" to="/item">
              Item 1
            </Link>
            <Link className="catagories" to="/item">
              Item 2
            </Link>
            <Link className="catagories" to="/item">
              Item 3
            </Link>
            <li className="catagories" to="/item">
              Item 4
            </li>
          </div>
        )}
      </div>
    </div>
  );
};

export default Dropdown;
