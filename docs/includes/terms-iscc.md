### **iscc**

!!! term "<small><http://purl.org/iscc/terms/#iscc></small>"

    An **ISCC-CODE** in canonical representation. This is the minimal required field for a valid ISCC Metadata object.

### **redirect**

!!! term "<small><http://purl.org/iscc/terms/#redirect></small>"

    URL to which a resolver should redirect an ISCC-ID that has been minted from a declartion that includes the IPFS-hash of this metadata instance.

### **previous**

!!! term "<small><http://purl.org/iscc/terms/#previous></small>"

    ISCC of the preceding version of this item.

### **properties**

!!! term "<small><http://purl.org/iscc/terms/#properties></small>"

    JSON or JSON-LD formated values about the identified *digital content*. Compatible with [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155).

### **filename**

!!! term "<small><http://purl.org/iscc/terms/#filename></small>"

    Filename of the referenced **digital content** (automatically used as fallback if the `name` field was not specified for ISCC processing)

### **fps**

!!! term "<small><http://purl.org/iscc/terms/#fps></small>"

    Frames per second of video assets.

### **width**

!!! term "<small><http://purl.org/iscc/terms/#width></small>"

    Width of visual media in number of pixels.

### **height**

!!! term "<small><http://purl.org/iscc/terms/#height></small>"

    Height of visual media in number of pixels.

### **characters**

!!! term "<small><http://purl.org/iscc/terms/#characters></small>"

    Number of text characters (code points after Unicode normalization)

### **parts**

!!! term "<small><http://purl.org/iscc/terms/#parts></small>"

    Indicates items that are part of this item via Content-Codes (inverse-property belongs).

### **part_of**

!!! term "<small><http://purl.org/iscc/terms/#part_of></small>"

    Indicates that this item is part of other items via their Content-Code.

### **features**

!!! term "<small><http://purl.org/iscc/terms/#features></small>"

    Granular features of the *digital content*.

### **datahash**

!!! term "<small><http://purl.org/iscc/terms/#datahash></small>"

    A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).

### **metahash**

!!! term "<small><http://purl.org/iscc/terms/#metahash></small>"

    A [Multihash](https://multiformats.io/multihash/) of the supplied metadata (default blake3). For deterministic results [JSC RFC5452](https://datatracker.ietf.org/doc/html/rfc8785) canonicalization is applied before hashing.

### **tophash**

!!! term "<small><http://purl.org/iscc/terms/#tophash></small>"

    A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).
