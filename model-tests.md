# Logo Model

- query: 

```sql
CREATE MODEL open_ai.logos
PREDICT img_url
USING
   engine = 'openai',
   mode = 'image',
   prompt_template = '{{text}}, 8K | highly detailed, modern, brand-specific logo style by Paula Scher combined with the iconic, retro logo style of James Modarelli | transparent background | bright colors';
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
