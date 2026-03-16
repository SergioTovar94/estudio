# Anotadores @

Los anotadores @ agregan metadata al código para que los frameworks como SpringBoot sepan como comportarse con las clases y atributos.

## Anotaciones de configuración de aplicación

```Java
@SpringBootApplication // Inicia toda la aplicación
```

## Anotadores de clases

```Java
@Entity // Esta clase representa una tabla en bases de datos
@Getter // Genera automáticamente los getters de todos los atributos
@Setter // Genera automáticamente los setters de todos los atributos
@NoArgsConstructor // Genera un constructor vacío
@Data // Recoge getters, setters, equals, hashCode, toString
@Table(name = table_name) // Si no se usa, define el nombre de la tabla igual a la clase.
```

# Anotadores de atributos

```Java
@Id // Define la llave primaria de la tabla
@GeneratedValue // Genera automáticamente el valor del ID
@Column // Define como se mapea la columna
@Enumerated // Se usa cuando un atributo es un Enum
```

# Anotadores de Controller

```Java
@RestController // Marca una clase como controlador Rest
@RequestMapping // Define la ruta base del enpoint
@GetMapping // Endpoint Get
@PostMapping // Endpoint Post
@PathVariable // Captura variables de la URL
@RequestBody // Convierte JSON en objeto Java
```

# Anotadores de Service

```Java
@Service // Marca como una capa de negocio
@Component // Anotación más general para registrar clases en el contenedor de Spring
```

# Anotaciones de Repository

```Java
@Repository // Indica que la clase maneja persistencia de datos
@Autowired // Permite que Spring realice inyección de dependencias
```

# Validaciones

```Java
@NotNull // Campo obligatorio
@NotBlank // Para String no vacíos
@Size // Longitud máxima o mínima
```

# Otras

```Java
@Builder // Permite crear objetos con patrón builder
```
