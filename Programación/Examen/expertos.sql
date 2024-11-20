-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-11-2024 a las 16:20:50
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ciencia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `expertos`
--

CREATE TABLE `expertos` (
  `Identificador` int(255) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `cargo` varchar(255) NOT NULL,
  `video` varchar(255) NOT NULL,
  `texto` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `expertos`
--

INSERT INTO `expertos` (`Identificador`, `titulo`, `cargo`, `video`, `texto`) VALUES
(1, 'Antonio Cano', 'Campanero y relojero en la catedral de Burgos', 'https://youtu.be/AH2BsxIB2ys?si=0XxpnVSdp8CBB0yv', 'Antonio Cano es campanero y relojero en la catedral de Burgos. Por sus manos han pasado muchas de las campanas y relojes de las iglesias de la provincia burgalesa, pero también de Canarias, donde ha pasado buen parte de su vida.\r\n\r\nA pesar de los cambios que ha sufrido su profesión, tanto por la automatización como porque muchas iglesias han dejado de tocar, sigue haciéndose cargo de las campanas y los relojes que siguen requiriendo mantenimiento, afinación y precisión.\r\n\r\nEn La ciencia que esconde la Catedral de Burgos nos muestra algunos de los secretos más escondidos de El Papamoscas, el genial autómata del templo que abre y cierra la boca a las horas, acompañado de El Martinillo, su ayudante a los carrillones. Cano nos enseña los mecanismos de estos ingenios mecánicos, que necesitan de conservación y mantenimiento, además de ayudarnos a comprender cómo se sincronizan con los relojes del templo.\r\n\r\n Además, en su labor como campanero nos acompaña a la cima de la catedral para ver cómo se tocan las campanas, hoy ya automatizadas, su estado y mantenimiento y su futuro.'),
(2, 'Constantino de la Fuente', 'Catedrático de secundaria y doctor en matemáticas', 'https://youtu.be/RHI6dUOBeVM?si=T6peBMhrb7RFqHyP', 'Constantino de la Fuente es catedrático de secundaria y doctor en matemáticas, además de presidente fundador de la Sociedad Castellana y Leonesa de Educación matemática Miguel de Guzmán.\r\n\r\nHa desarrollado una intensa carrera investigadora con numerosos artículos en revistas científicas, además de conferencias en jornadas y congresos, todo ello mientras desarrollaba su actividad docente en el IES Cardenal López de Mendoza.  De la Fuente es autor de dos libros sobre matemáticas en la catedral de Burgos y ha destacado por su implicación en la divulgación de la cultura científica y matemática entre los más jóvenes.\r\n\r\nEn La ciencia que esconde la Catedral de Burgos, De la Fuente nos guía por los secretos matemáticos que esconde el templo, tanto en su construcción como en su decoración. Proporciones como el número áureo, el rectángulo de plata o la proporción cordobesa se encuentran en algunos de los lugares más emblemáticos de la catedral, como el rosetón del Sarmental, la escalera dorada y el cimborrio la combinación de sus octógonos. \r\n\r\nEstas proporciones también pueden albergar un significado religioso, como en la vesica piscis, la intersección entre dos círculos que se utilizó como símbolo de Cristo entre los primeros creyentes. Todas estas proporciones, formas geométricas y algebraicas revelan una comprensión de las matemáticas muy precisa que llega a su punto más alto con la Escalera dorada. La obra de Diego de Siloé está inspirada en el renacimiento italiano y en su construcción alberga un sinfín de proporciones relacionadas que le permiten ser una solución arquitectónica brillante y, al mismo tiempo, una obra armónica que ha deslumbrado a arquitectos de todo el mundo.\r\n\r\nPor último, nos enseña que en las proporciones también puede haber ecos de otras culturas, como en el Cimborrio de la catedral, donde el arte mozárabe está presente en algunas de las relaciones y proporciones que conforman esta obra de arte barroca.'),
(3, 'Enrique Barrio', 'Maestro vidriero. Ha restaurado y recreado vidrieras en la catedral', 'https://youtu.be/fQ_t4d-z7vM?si=THqyQFeuru6vtjZT', 'Enrique Barrio es maestro vidriero y ha colaborado en la restauración y recreación de varias vidrieras en la catedral de Burgos. Con formación tanto en la técnica de las vidrieras como en estudios históricos sobre el vidrio, colabora habitualmente en publicaciones y proyectos científicos, así como en la difusión de su trabajo a través de conferencias para dar a conocer la importancia del mantenimiento y la conservación del patrimonio artístico.\r\n\r\nAdemás de en la catedral de Burgos, ha realizado actuaciones en las catedrales de Astorga, Mallorca, Orense y Cienfuegos (Cuba) y mantiene formas de trabajo tradicionales para la creación y conservación de los vitrales. Para realizar las labores de conservación, Enrique Barrio realiza un estudio de las características físicas y químicas de cada vidrio completo, sus materiales y los problemas de degradación y deterioro que presenta.\r\n\r\nEn La ciencia que esconde la Catedral de Burgos, Barrio nos muestra su trabajo en el taller, en el que mantiene las formas de creación, pintura, corte y emplomado tradicionales y que resultan fundamentales para que se mantenga la esencia y el aspecto de las vidrieras tradicionales del templo, que, además, suponen una enorme muestra del recorrido histórico del arte de la vidriera a lo largo de los siglos. Además, nos enseña los criterios a la hora del mantenimiento y sustitución de los vitrales.'),
(4, 'Francisco del Hoyo', 'Restaurador de pinturas y policromías', 'https://youtu.be/zCSYopOCNQY?si=IBFvZUZTMcQnkPas', 'Francisco Jesús del Hoyo es licenciado en Bellas Artes y restaurador de pinturas y policromías. Con una amplia experiencia de trabajo dentro de la Catedral de Burgos. Especialista en policromías de piedra y madera, lleva varios años trabajando en el interior de la seo burgalesa, además de mantener una intensa actividad como artista plástico.\r\n\r\nEn La ciencia que esconde la Catedral de Burgos nos enseña la técnica de la policromía, el pintado sobre madera o piedra, y cómo se ha utilizado para ennoblecer materiales, hacerlos destacar o embellecer la decoración. Este proceso, diferente a la pintura sobre lienzo o el fresco, requiere de mucha atención y cuidados para evitar su deterioro.\r\n\r\nLos diferentes procesos químicos, la presencia de los humos de incienso y el propio paso del tiempo deterioran estas capas de pintura, muchas veces de tal forma que es imposible recuperar los colores originales. Sin embargo, un trabajo detallado permite sacar de nuevo a la luz la riqueza cromática de la catedral de Burgos.\r\n\r\nEl proceso de restauración de las obras va desde los análisis químicos hasta procesos de recuperación físicos y químicos, llegando incluso a utilizar el láser para limpiar la piedra no pintada o mezclas de componentes químicos para las superficies policromadas, muchas veces con una mezcla hecha a medida para cada detalle de la obra.\r\n\r\nDel Hoyo nos lleva de la mano por un proceso que une arte y ciencia en el que el restaurador trata de ser invisible y cubrir sus huellas para mantener la esencia original de cada pintura y escultura.'),
(13, 'bb', 'bb', 'bb', 'bb'),
(14, 'aa', 'aa', 'aa', 'aa'),
(15, 'aa', 'aa', 'aa', 'aa');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `expertos`
--
ALTER TABLE `expertos`
  ADD PRIMARY KEY (`Identificador`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `expertos`
--
ALTER TABLE `expertos`
  MODIFY `Identificador` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
