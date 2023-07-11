# Logo Model

- query: 

```sql
CREATE MODEL open_ai.logo_mod_2
PREDICT img_url
USING
   engine = 'openai',
   mode = 'image',
   prompt_template = '{{text}}, 8K | highly detailed, modern, brand-specific logo style by Paula Scher combined with the abstract, colorful logo design style of Tinker Hatfield | transparent background | bright colors';
```

```sql
CREATE MODEL open_ai.logos
PREDICT img_url
USING
   engine = 'openai',
   mode = 'image',
   prompt_template = '{{text}}, 8K | highly detailed, modern, brand-specific logo style by Paula Scher combined with the iconic, retro logo style of James Modarelli | transparent background | bright colors'
```

SELECT * 
FROM open_ai.logo_mod 
WHERE text = 'A logo depicting the brand name, "Hue" in bold, black, letters underneath a colorful, purple paint drop icon.';

-- CREATE MODEL open_ai.logo_mod
-- PREDICT img_url
-- USING
--    engine = 'openai',
--    mode = 'image',
--    prompt_template = '{{text}}, 8K | highly detailed, modern, brand-specific logo style by Paula Scher combined with the iconic, retro logo style of James Modarelli | transparent background | bright colors';

-- SELECT * 
-- FROM open_ai.logo_mod 
-- WHERE text = .';


```sql
CREATE MODEL open_ai.logo_mod_2
PREDICT img_url
USING
   engine = 'openai',
   mode = 'image',
   prompt_template = '{{text}}, 8K | highly detailed, modern, brand-specific logo style by Paula Scher combined with the abstract, colorful logo design style of Tinker Hatfield | transparent background | bright colors';
```
SELECT * 
FROM open_ai.logo_mod_2 
WHERE text = 'A logo for an art store with the brand name, "Hue" in bold, letters. The logo text has colorful, paint splatters on it';

SELECT * 
FROM open_ai.logo_mod_2 
WHERE text = 'A vector based logo with a transparent background for a computer and software company named "BPS"';