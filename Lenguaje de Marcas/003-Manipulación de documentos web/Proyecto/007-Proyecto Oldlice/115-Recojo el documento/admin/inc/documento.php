<?php if(isset($_GET['documento'])){?>
	<h1>Pedido</h1>
	<table>
		<tr>
			<td width=50%>
				<h2>Emisor</h2>
				<h3>FabriCraft - Joshué Daniel Freire Sánchez</h3>
				<p>calle francisco climent 8</p>
				<p>46007 Valencia</p>
				<p>Y8562933R</p>
				<p>info@daniel.com</p>
			</td>
			<td>
				<h2>Receptor</h2>
				<h3>Nombre del cliente</h3>
				<p>Calle del cliente</p>
				<p>Codigo postal y poblacion</p>
				<p>DNI</p>
				<p>emaildelcliente@fabricraft.com</p>
			</td>
		</tr>
		<tr>
			<td>
				<h2>Fecha de la factura</h2>
				<p>2024-12-12</p>
			</td>
			<td>
				<h2>Número de la factura</h2>
				<p>20241212432</p>
			</td>
		</tr>
		<tr>
			<td colspan=2>
				<h2>Lineas de pedido</h2>
			</td>
			<table>
				<tr>
					<th>Nombre</th>
					<th>Descripcion</th>
					<th>Precio</th>
				</tr>
				<tr>
					<td>aaa</td>
					<td>aaaa</td>
					<td>aaa</td>
				</tr>
				<tr>
					<td>aaa</td>
					<td>aaaa</td>
					<td>aaa</td>
				</tr>
				<tr>
					<td>aaa</td>
					<td>aaaa</td>
					<td>aaa</td>
				</tr>
				<tr>
					<td>aaa</td>
					<td>aaaa</td>
					<td>aaa</td>
				</tr>
				<tr>
					<td>aaa</td>
					<td>aaaa</td>
					<td>aaa</td>
				</tr>
				<tr>
					<td colspan=2>Total</td>
					<td>4324</td>
				</tr>
			</table>
		</tr>
	</table>
	
<?php } ?>