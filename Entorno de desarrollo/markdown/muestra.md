# Entorno de desarrollo 
## Documentación de un programa 
****
- Para saber acerca de lo que nos están ofreciendo de una manera detallada para el programador pueda ver en que carpeta debe ingresar se diseñó

![ALT Documentación](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/932801ee728bf35aba50ec08254532d39c0fac49/Entorno%20de%20desarrollo/imagenes/Captura.PNG)

1. Tenemos la funcion que extrae los docstring de los documentos

function extractDocstring($filePath) {
    $content = file_get_contents($filePath);
    $extension = pathinfo($filePath, PATHINFO_EXTENSION);
    
 ``` 
    switch ($extension) {
        case 'php':
            // Match comments following the opening <?php tag
            if (preg_match('/<\\?php\\s*\\/\\*\\*(.*?)\\*\\//s', $content, $matches) ||
                preg_match('/<\\?php\\s*\\/\\*(.*?)\\*\\//s', $content, $matches)) {
                return trim($matches[1]);
            }
            break;

        case 'js':
        case 'css':
        case 'java':
        case 'c':
        case 'cpp':
            // Match comments enclosed in /* ... */
            if (preg_match('/\\/\\*(.*?)\\*\\//s', $content, $matches)) {
                return trim($matches[1]);
            }
            break;

        case 'py':
            // Match Python docstrings (""" ... """ or single-line # comments)
            if (preg_match('/^\s*"""(.*?)"""/s', $content, $matches)) {
                return trim($matches[1]);
            } elseif (preg_match('/^\s*#\s*(.+)$/m', $content, $matches)) {
                return trim($matches[1]);
            }
            break;

        case 'html':
        case 'htm':
            // Match HTML comments <!-- ... -->
            if (preg_match('/<!--(.*?)-->/s', $content, $matches)) {
                return trim($matches[1]);
            }
            break;

        default:
            return '';
    }
 ``` 
