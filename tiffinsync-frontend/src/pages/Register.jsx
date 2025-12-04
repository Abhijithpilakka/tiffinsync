import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [formData, setFormData] = useState({
    name: "",
    role: "user",
    address: "",
    latitude: "",
    longitude: "",
  });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleRegister = (e) => {
    e.preventDefault();
    // TODO: Call backend `/auth/register` with formData
    
    console.log("Registering user:", formData);

    // After successful registration
    navigate("/dashboard");
  };

  return (
    <div style={styles.container}>
      <h2>Complete Registration</h2>
      <form onSubmit={handleRegister} style={styles.form}>
        <input
          type="text"
          name="name"
          placeholder="Full Name"
          value={formData.name}
          onChange={handleChange}
          required
          style={styles.input}
        />
        <select
          name="role"
          value={formData.role}
          onChange={handleChange}
          style={styles.input}
        >
          <option value="user">User</option>
          <option value="provider">Provider</option>
        </select>
        <input
          type="text"
          name="address"
          placeholder="Address"
          value={formData.address}
          onChange={handleChange}
          style={styles.input}
        />
        <input
          type="text"
          name="latitude"
          placeholder="Latitude"
          value={formData.latitude}
          onChange={handleChange}
          style={styles.input}
        />
        <input
          type="text"
          name="longitude"
          placeholder="Longitude"
          value={formData.longitude}
          onChange={handleChange}
          style={styles.input}
        />
        <button type="submit" style={styles.button}>Register</button>
      </form>
    </div>
  );
};

const styles = {
  container: { display: "flex", flexDirection: "column", alignItems: "center", marginTop: "50px" },
  form: { display: "flex", flexDirection: "column", gap: "10px", width: "250px" },
  input: { padding: "10px", fontSize: "16px" },
  button: { padding: "10px", background: "#28a745", color: "white", border: "none", cursor: "pointer" },
};

export default Register;