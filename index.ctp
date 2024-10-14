<h1 class="title_line_color blue">Agropartes</h1>
<div id="product_index" class="contain product_catalogo product clearfix">
    <?php echo $this->element('form-search-catalogo-agro'); ?>
    <div class="product_index_container clearfix">
        <?php if (empty($products)) : ?>
            <p class="center">No hay productos encontrados</p>
        <?php else : ?>
            <div class="table-responsive">
                <table class="table">
                    <tr>
                        <th>Modelo</th>
                        <th>Código Catalano</th>
                        <th>Dientes</th>
                        <th>Med Cub</th>
                        <th>Diam Int (MM)</th>
                        <th>Diám E.C.</th>
                        <th>CantxDiámAg</th>
                        <th>Esp (mm)</th>
                        <th>Marca</th>
                        <th>Observación</th>
                        <th>Imagen</th>
                    </tr>
                    <?php foreach ($products as $key => $product) : ?>
                        <tr>
                            <td><?php echo  $product['AgroProduct']['modelo']; ?></td>
                            <td><?php echo  $product['AgroProduct']['id_catalano']; ?></td>
                            <td><?php echo  $product['AgroProduct']['dtes']; ?></td>
                            <td><?php echo  $product['AgroProduct']['med_cub']; ?></td>
                            <td><?php echo  $product['AgroProduct']['diam_int']; ?></td>
                            <td><?php echo  $product['AgroProduct']['diam_ex']; ?></td>
                            <td><?php echo  $product['AgroProduct']['can_diam']; ?></td>
                            <td><?php echo  $product['AgroProduct']['esp_mm']; ?></td>
                            <td style="max-width: 200px; overflow-wrap: break-word; "><?php echo  $product['AgroProduct']['marca']; ?></td>
                            <td style="max-width: 200px; overflow-wrap: break-word; "><?php echo  $product['AgroProduct']['observacion']; ?></td>
                            <td><?php if (!empty($product['AgroProduct']['imagen']) and file_exists('img/productImg/' . $product['AgroProduct']['imagen'])) { ?>
                                    <a class="brw_image" href="<?php echo Router::url('/img/productImg/' . $product['AgroProduct']['imagen']); ?>">imagen</a>
                                <?php } ?>
                            </td>
                        </tr>
                    <?php endforeach; ?>
                </table>
            </div>
        <?php endif; ?>

    </div>
</div>