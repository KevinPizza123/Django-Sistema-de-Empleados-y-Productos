import React, { useState, useEffect } from 'react';

function ListaEmpleados() {
  const [empleados, setEmpleados] = useState([]);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchEmpleados = async () => {
      try {
        const response = await fetch('http://localhost:8000/empleados/api/empleados/'); // Reemplaza con la URL de tu API
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setEmpleados(data);
        setIsLoading(false);
      } catch (error) {
        setError(error);
        setIsLoading(false);
      }
    };

    fetchEmpleados();
  }, []); // El array vacío como segundo argumento asegura que el efecto se ejecute solo una vez al montar el componente

  if (isLoading) {
    return <div>Cargando empleados...</div>;
  }

  if (error) {
    return <div>Error al cargar empleados: {error.message}</div>;
  }

  return (
    <div>
      <h1>Lista de Empleados</h1>
      {empleados.length > 0 ? (
        <ul>
          {empleados.map(empleado => (
            <li key={empleado.id}>
              {empleado.nombre} {empleado.apellido} - Cédula: {empleado.numero_de_cedula}
            </li>
          ))}
        </ul>
      ) : (
        <p>No hay empleados registrados.</p>
      )}
    </div>
  );
}

export default ListaEmpleados;