# Text format schema

A JSON Schema for expressing formatted text with styling metadata.

## Schema Structure

The schema defines a format for representing styled text with the following components:

- **Version**: Semantic versioning for schema compatibility (`version`)
- **Metadata**: Array of key-value pairs for general metadata (`meta`)
- **Data**: Array of styled text objects (`data`)
  - `txt`: Required Unicode text content
  - `st`: Optional styling object with background (`bg`), foreground (`fg`), and bit flags (`fl`)
- **Extensions**: Reserved space for future enhancements (`ext`)

## Properties

### Styling Object (`st`)
- `bg`: Background color as hex string (`#RRGGBB`)
- `fg`: Foreground color as hex string (`#RRGGBB`)
- `fl`: Integer bit flag field for text formatting


