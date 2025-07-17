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

#### Flag field (`fl`)

16 bit unsigned integer with the following bit assignments:

##### bit 15-8 (MSB)

| 15  | 14  | 13  | 12  | 11  | 10  |  9  |  8  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |

Bit 15-8 unused

##### bit 7-0 (LSB)

|  7  |  6  |  5  |  4  |      3       |     2     |   1    |  0   |
| :-: | :-: | :-: | :-: | :----------: | :-------: | :----: | :--: |
|  -  |  -  |  -  |  -  | striketrough | underline | italic | bold |

Bit 7-4 unused

