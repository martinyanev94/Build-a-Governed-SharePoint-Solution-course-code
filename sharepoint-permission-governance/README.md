# Permission governance prototype

Run the matrix acceptance check with:

```bash
python3 src/permission_matrix.py
```

Expected output:

```text
matrix is valid
```

The matrix models site defaults for Northstar Owners, Northstar Members, and Northstar Visitors. HR Records is the smallest boundary that needs a different audience, so its inherited access is replaced with an HR Records group at the library boundary.
