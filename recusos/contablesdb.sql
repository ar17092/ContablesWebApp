-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 09-01-2021 a las 00:30:27
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `contablesdb`
--

-- --------------------------------------------------------


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuenta`
--

CREATE TABLE `cuenta` (
  `id_cuenta` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `id_tipocuenta` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cuenta`
--

INSERT INTO `cuenta` (`id_cuenta`, `nombre`, `descripcion`, `id_tipocuenta`) VALUES
(1, 'Efectivos y equivalentes', 'Efectivos', 1),
(4, 'IVA debito fiscal', 'impuesta iva', 8),
(7, 'Cuenta nueva', 'Nueva', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE `empresa` (
  `id_empresa` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `id_rubro` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empresa`
--

INSERT INTO `empresa` (`id_empresa`, `nombre`, `id_rubro`) VALUES
(1, 'ABC', 1),
(5, 'Empresa Klaus', 10),
(6, 'OVNICO S.A DE C.V', 11),
(7, 'Mike company', 12),
(8, 'Diego company', 13);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro__diario`
--

CREATE TABLE `libro__diario` (
  `id_libro_diario` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `libro__diario`
--

INSERT INTO `libro__diario` (`id_libro_diario`, `nombre`, `descripcion`, `id_user`) VALUES
(1, 'Primer libro diario', 'Soy aragon598 este es mi primer ldiario', 2),
(2, 'LDiario de diego', 'Este es de la empresa de Diego', 3),
(8, 'Daisy Ldiario', 'Mi primer libro diario', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partida`
--

CREATE TABLE `partida` (
  `id_partida` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `valor_debe` float DEFAULT NULL,
  `valor_haber` float DEFAULT NULL,
  `id_ldiario` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `partida`
--

INSERT INTO `partida` (`id_partida`, `nombre`, `valor_debe`, `valor_haber`, `id_ldiario`, `fecha`) VALUES
(1, 'aragon-partida-1', 65.61, 55.21, 1, '2019-11-04'),
(2, 'diego-partida-1', 0, 0, 2, '2018-01-04'),
(3, 'aragon-partida-2', 146, 146, 1, '2019-11-11'),
(4, 'daysi-primera-partida', 12, 12, 8, '2018-11-13'),
(5, 'tercera-partida', 0, 0, 1, '2018-11-20');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partida_concepto`
--

CREATE TABLE `partida_concepto` (
  `id_pconcepto` int(11) NOT NULL,
  `valor_parcial` float DEFAULT NULL,
  `id_cuenta` int(11) DEFAULT NULL,
  `id_partida` int(11) DEFAULT NULL,
  `cargo_abono` tinyint(1) DEFAULT NULL
) ;

--
-- Volcado de datos para la tabla `partida_concepto`
--

INSERT INTO `partida_concepto` (`id_pconcepto`, `valor_parcial`, `id_cuenta`, `id_partida`, `cargo_abono`) VALUES
(2, 10.4, 1, 1, 1),
(3, 50.21, 4, 1, 1),
(6, 5, 7, 1, 1),
(8, 105, 1, 3, 1),
(9, 64, 4, 3, 0),
(10, 41, 7, 3, 1),
(11, 65.61, 7, 1, 0),
(13, 12, 1, 4, 1),
(14, 12, 4, 4, 0),
(15, 82, 7, 3, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rubro`
--

CREATE TABLE `rubro` (
  `id_rubro` int(11) NOT NULL,
  `rubro` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `rubro`
--

INSERT INTO `rubro` (`id_rubro`, `rubro`) VALUES
(1, 'Construccion'),
(2, 'comercio'),
(5, 'Ventas'),
(8, 'Cualquiera'),
(9, 'Rubro diego'),
(10, 'Klaus rubro'),
(11, 'Comunicaciones'),
(12, 'mike rubro'),
(13, 'Diego rubro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `subcuenta`
--

CREATE TABLE `subcuenta` (
  `id_subcuenta` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `id_cuenta` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `subcuenta`
--

INSERT INTO `subcuenta` (`id_subcuenta`, `nombre`, `descripcion`, `id_cuenta`) VALUES
(1, 'Caja general', 'xd', 1),
(4, 'IVA debito fiscal local', 'impuesto iva local', 4),
(5, 'IVA debito fiscal externo', 'Pasivo', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_cuenta`
--

CREATE TABLE `tipo_cuenta` (
  `id_tipo_cuenta` int(11) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `saldo` tinyint(1) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ;

--
-- Volcado de datos para la tabla `tipo_cuenta`
--

INSERT INTO `tipo_cuenta` (`id_tipo_cuenta`, `nombre`, `saldo`, `descripcion`) VALUES
(1, 'Activo', 1, 'De tipo acreedor'),
(7, 'Patrimonio', 1, NULL),
(8, 'Pasivo', 0, NULL),
(10, 'Cuenta deudoras', 0, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(128) NOT NULL,
  `empresa_id` int(11) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL
) ;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `nombre`, `username`, `password`, `empresa_id`, `is_admin`) VALUES
(1, 'ADMIN', 'admin', 'pbkdf2:sha256:150000$5oClIM0i$c155be080802a2299bf20f891ea9e542c8fb11ea4a5927d390c36d2d91252a60', NULL, 1),
(2, 'Alejandro Aragon', 'aragon598', 'pbkdf2:sha256:150000$5oClIM0i$c155be080802a2299bf20f891ea9e542c8fb11ea4a5927d390c36d2d91252a60', 1, 0),
(3, 'Diego Rugamas', 'rugamas08', 'pbkdf2:sha256:150000$beAlUki6$0ebf2d83ec98b673ffa5311135ea8a87cdf710cb6ba107eaba9cdde0efdab299', 8, 0),
(5, 'Klaus Montano', 'montano', 'pbkdf2:sha256:150000$7TTu3ezr$596b30ee0894aaa4aa9fd786581fc3ce944725fa6ca5717c2fc6270dbd6dfe40', 5, 0),
(6, 'Daysi Rugamas', 'daysi65', 'pbkdf2:sha256:150000$8FU5AJtF$6153b6bc738cb2432d5fb5d50b3ab9fdeb03038375c16957ee776439ad8eebfb', 6, 0),
(7, 'Mike Aragón', 'mike64', 'pbkdf2:sha256:150000$d3paWwIK$c2a33c9213ce59854a28b081026a9f707dd344aec46deede4f27570a62504eac', 7, 0);

--
-- Índices para tablas volcadas
--


--
-- Indices de la tabla `cuenta`
--
ALTER TABLE `cuenta`
  ADD PRIMARY KEY (`id_cuenta`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `id_tipocuenta` (`id_tipocuenta`);

--
-- Indices de la tabla `empresa`
--
ALTER TABLE `empresa`
  ADD PRIMARY KEY (`id_empresa`),
  ADD KEY `id_rubro` (`id_rubro`);

--
-- Indices de la tabla `libro__diario`
--
ALTER TABLE `libro__diario`
  ADD PRIMARY KEY (`id_libro_diario`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `id_user` (`id_user`);

--
-- Indices de la tabla `partida`
--
ALTER TABLE `partida`
  ADD PRIMARY KEY (`id_partida`),
  ADD KEY `id_ldiario` (`id_ldiario`);

--
-- Indices de la tabla `partida_concepto`
--
ALTER TABLE `partida_concepto`
  ADD PRIMARY KEY (`id_pconcepto`),
  ADD KEY `id_cuenta` (`id_cuenta`),
  ADD KEY `id_partida` (`id_partida`);

--
-- Indices de la tabla `rubro`
--
ALTER TABLE `rubro`
  ADD PRIMARY KEY (`id_rubro`);

--
-- Indices de la tabla `subcuenta`
--
ALTER TABLE `subcuenta`
  ADD PRIMARY KEY (`id_subcuenta`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `id_cuenta` (`id_cuenta`);

--
-- Indices de la tabla `tipo_cuenta`
--
ALTER TABLE `tipo_cuenta`
  ADD PRIMARY KEY (`id_tipo_cuenta`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `empresa_id` (`empresa_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cuenta`
--
ALTER TABLE `cuenta`
  MODIFY `id_cuenta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `empresa`
--
ALTER TABLE `empresa`
  MODIFY `id_empresa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `libro__diario`
--
ALTER TABLE `libro__diario`
  MODIFY `id_libro_diario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `partida`
--
ALTER TABLE `partida`
  MODIFY `id_partida` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `partida_concepto`
--
ALTER TABLE `partida_concepto`
  MODIFY `id_pconcepto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rubro`
--
ALTER TABLE `rubro`
  MODIFY `id_rubro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `subcuenta`
--
ALTER TABLE `subcuenta`
  MODIFY `id_subcuenta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `tipo_cuenta`
--
ALTER TABLE `tipo_cuenta`
  MODIFY `id_tipo_cuenta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cuenta`
--
ALTER TABLE `cuenta`
  ADD CONSTRAINT `cuenta_ibfk_1` FOREIGN KEY (`id_tipocuenta`) REFERENCES `tipo_cuenta` (`id_tipo_cuenta`) ON DELETE SET NULL;

--
-- Filtros para la tabla `empresa`
--
ALTER TABLE `empresa`
  ADD CONSTRAINT `empresa_ibfk_1` FOREIGN KEY (`id_rubro`) REFERENCES `rubro` (`id_rubro`) ON DELETE SET NULL;

--
-- Filtros para la tabla `libro__diario`
--
ALTER TABLE `libro__diario`
  ADD CONSTRAINT `libro__diario_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE SET NULL;

--
-- Filtros para la tabla `partida`
--
ALTER TABLE `partida`
  ADD CONSTRAINT `partida_ibfk_1` FOREIGN KEY (`id_ldiario`) REFERENCES `libro__diario` (`id_libro_diario`) ON DELETE CASCADE;

--
-- Filtros para la tabla `partida_concepto`
--
ALTER TABLE `partida_concepto`
  ADD CONSTRAINT `partida_concepto_ibfk_1` FOREIGN KEY (`id_cuenta`) REFERENCES `cuenta` (`id_cuenta`) ON DELETE SET NULL,
  ADD CONSTRAINT `partida_concepto_ibfk_2` FOREIGN KEY (`id_partida`) REFERENCES `partida` (`id_partida`) ON DELETE SET NULL;

--
-- Filtros para la tabla `subcuenta`
--
ALTER TABLE `subcuenta`
  ADD CONSTRAINT `subcuenta_ibfk_1` FOREIGN KEY (`id_cuenta`) REFERENCES `cuenta` (`id_cuenta`) ON DELETE SET NULL;

--
-- Filtros para la tabla `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`empresa_id`) REFERENCES `empresa` (`id_empresa`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
