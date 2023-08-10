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
WHERE text = 'A logo for a technology company with the brand name, "Bits" in bold, black letters. There is green matrix code inside of the letters.';

SELECT * 
FROM open_ai.logo_mod_2 
WHERE text = 'A vector based logo with a transparent background for a computer and software company named "BPS"';


```sql
SELECT * 
FROM open_ai.logo_mod
WHERE text = 'A logo for a technology company with the brand name, "Bits" in bold, black letters. There is green matrix code inside of the letters.';
```


```sql
CREATE MODEL open_ai.icons
PREDICT img_url
USING
   engine = 'openai',
   mode = 'image',
   prompt_template = '{{text}}, 16x16 pixels | simple, gradient and fill line icon style by Adobe Stock and Shutterstuck | transparent background | bright colors';
```

```sql
CREATE MODEL open_ai.logos
PREDICT img_url
USING
   engine = 'openai',
   mode = 'image',
   prompt_template = '{{text}}, 8K | highly detailed, modern, brand-specific logo style by Paula Scher combined with the iconic, retro logo style of James Modarelli | transparent background | bright colors'
```

```sql
SELECT * 
FROM open_ai.logos 
WHERE text = 'A logo depicting the brand name, "Hue" underneath a colorful, purple paint drop icon.';
```

```sql
SELECT * 
FROM open_ai.logo_mod
WHERE text = 'A logo for a technology company with the brand name, "Bits" in bold, black letters. Circuit board designs are inside of the letters.';
```
```sql
'A vector based logo displaying the brand name, "Bits" in bold, black, letters. Circuit board design mixed into the letters. Transparent background.';
```
```sql
SELECT * 
FROM open_ai.icons
WHERE text = 'A purple gradient paint splatter icon';
```



CREATE MODEL open_ai.urban
PREDICT img_url
USING
   engine = 'openai',
   mode = 'image',
   prompt_template = '{{text}}, 4K | highly detailed, contemporary, urban street art style of Kaws combined with the controversial style of Banksy | bright lighting | warrm happy colors | 1024 x 1024 pixels';



CREATE MODEL open_ai.urban
PREDICT img_url
USING
engine = 'openai',
mode = 'image',
prompt_template = '{{text}}, 4K | highly detailed, contemporary, urban street art style of KAWS combined with the controversial style of Banksy | bright lighting | warrm happy colors | 1024 x 1024 pixels',
api_key = 'sk-******';



SELECT *
FROM open_ai.urban_art
WHERE text='A statue of a cool mouse with headphones, baggy pants, and a t-shirt on a side-street in NYC.'

"A statue of a cool using turn tables on the lower east side of Manhattan"




