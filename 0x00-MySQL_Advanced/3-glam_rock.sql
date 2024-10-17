-- This script lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name,
       IFNULL(YEAR('2022-01-01') - YEAR_FORMED, 0) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC
