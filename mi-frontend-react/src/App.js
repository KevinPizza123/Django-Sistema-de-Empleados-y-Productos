import React from 'react';
import ListaEmpleados from './ListaEmpleados'; // Importa el componente que creaste

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Mi Sistema de Inventario y Empleados</h1>
      </header>
      <main>
        <ListaEmpleados /> {/* Renderiza el componente ListaEmpleados */}
      </main>
    </div>
  );
}

export default App;