import re
import base64
import random
import string

class LuaObfuscator:
    def __init__(self):
        self.junk_keywords = ['local', 'if', 'then', 'else', 'end', 'function', 'return']
        self.junk_names = ['_'.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(100)]
    
    def obfuscate(self, code: str, level: str = 'medium') -> str:
        """Obfuscate Lua code based on protection level"""
        
        if level == 'light':
            return self._light_obfuscate(code)
        elif level == 'medium':
            return self._medium_obfuscate(code)
        elif level == 'heavy':
            return self._heavy_obfuscate(code)
        else:
            return code
    
    def _remove_comments(self, code: str) -> str:
        """Remove single and multi-line comments"""
        # Remove single-line comments
        code = re.sub(r'--.*?$', '', code, flags=re.MULTILINE)
        
        # Remove multi-line comments
        code = re.sub(r'--\[\[.*?\]\]', '', code, flags=re.DOTALL)
        
        return code
    
    def _minify(self, code: str) -> str:
        """Minify code by removing unnecessary whitespace"""
        # Remove leading/trailing whitespace from lines
        lines = code.split('\n')
        lines = [line.strip() for line in lines if line.strip()]
        
        # Remove empty lines
        code = '\n'.join(lines)
        
        # Remove extra spaces around operators
        code = re.sub(r'\s*([=+\-*/<>(){}\[\],:;])\s*', r'\1', code)
        code = re.sub(r'([a-zA-Z0-9_])\s+([a-zA-Z0-9_])', r'\1 \2', code)
        
        return code
    
    def _rename_variables(self, code: str) -> str:
        """Rename variables to make code harder to read"""
        # Find all variable assignments (very basic)
        variables = set(re.findall(r'local\s+([a-zA-Z_][a-zA-Z0-9_]*)', code))
        variables.update(re.findall(r'function\s+([a-zA-Z_][a-zA-Z0-9_]*)', code))
        
        # Create mapping to obfuscated names
        var_map = {}
        for var in variables:
            if var not in ['print', 'table', 'math', 'string', 'os', 'io']:  # Preserve common functions
                obf_name = 'v' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
                var_map[var] = obf_name
        
        # Replace variables in code
        for original, obfuscated in var_map.items():
            code = re.sub(r'\b' + original + r'\b', obfuscated, code)
        
        return code
    
    def _encrypt_strings(self, code: str) -> str:
        """Encrypt strings using Base64 and create a decryption wrapper"""
        # Find all strings
        strings = re.findall(r'(["\'])([^"]*?)\1', code)
        
        if not strings:
            return code
        
        # Create decryption function
        decode_func = '''local function d(s)return string.char(tonumber(string.sub(s,1,2),16),tonumber(string.sub(s,3,4),16))..d(string.sub(s,5))or''end'''
        
        # Encrypt strings
        for quote, string_content in strings:
            encrypted = self._simple_encrypt(string_content)
            encoded_string = quote + encrypted + quote
            original_string = quote + string_content + quote
            code = code.replace(original_string, encoded_string, 1)
        
        return code
    
    def _simple_encrypt(self, text: str) -> str:
        """Simple encryption using hex encoding"""
        hex_str = ''.join(f'{ord(c):02x}' for c in text)
        return hex_str
    
    def _add_junk_code(self, code: str) -> str:
        """Add meaningless code to confuse decompilers"""
        junk_lines = [
            'local _=0for i=1,0 do _=_+1 end',
            'if false then print("never")end',
            'local t={}t[0]=0',
        ]
        
        # Insert junk at random points
        lines = code.split('\n')
        for _ in range(min(len(lines) // 5, 3)):
            insert_pos = random.randint(0, len(lines) - 1)
            lines.insert(insert_pos, random.choice(junk_lines))
        
        return '\n'.join(lines)
    
    def _light_obfuscate(self, code: str) -> str:
        """Light obfuscation: remove comments + minify"""
        code = self._remove_comments(code)
        code = self._minify(code)
        return code
    
    def _medium_obfuscate(self, code: str) -> str:
        """Medium obfuscation: light + variable renaming"""
        code = self._light_obfuscate(code)
        code = self._rename_variables(code)
        return code
    
    def _heavy_obfuscate(self, code: str) -> str:
        """Heavy obfuscation: everything + encryption + junk code"""
        code = self._medium_obfuscate(code)
        code = self._encrypt_strings(code)
        code = self._add_junk_code(code)
        return code
