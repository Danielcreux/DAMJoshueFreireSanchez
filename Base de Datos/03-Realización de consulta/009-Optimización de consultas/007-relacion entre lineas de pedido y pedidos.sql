ALTER TABLE `lineaspedido` 
ADD CONSTRAINT `lineasapedidos` 
FOREIGN KEY (`pedidos_fecha`) 
REFERENCES `pedidos`(`Identificador`) 
ON DELETE RESTRICT 
ON UPDATE RESTRICT;